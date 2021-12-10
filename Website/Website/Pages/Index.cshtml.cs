using CsvHelper;
using CsvHelper.Configuration;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Tweetinvi;
using Website.Models;
using AutoMapper;
using System.Globalization;
using System.Text;

namespace Website.Pages
{
    public class IndexModel : PageModel
    {
        private readonly ILogger<IndexModel> _logger;

        public IndexModel(ILogger<IndexModel> logger)
        {
            _logger = logger;
            CandidateList = new Dictionary<string, string>()
            {
                {"n_arthaud", "Nathalie Arthaud"},
                {"upr_asselineau", "François Asselineau"},
                {"dupontaignan", "Nicolas Dupont-Aignan"},
                {"Anne_Hidalgo","Anne Hidalgo"},
                {"yjadot","Yannick Jadot"},
                {"jeanlassalle","Jean Lassalle"},
                {"MLP_officiel","Marine Le Pen"},
                {"JLMelenchon","Jean-Luc Mélenchon"},
                {"montebourg","Arnaud Montebourg"},
                {"jfpoisson78","Jean-Frédéric Poisson"},
                {"PhilippePoutou","Philippe Poutou"},
                {"Fabien_Roussel","Fabien Roussel"},
                //{"","Antoine Waechter"}
            };
            TweetCount = 0;
        }

        public Dictionary<string, string> CandidateList { get; set; }
        public List<TweetModel> TweetsList { get; set; } = new List<TweetModel>();

        [BindProperty]
        public string TwitterId { get; set; }
        [BindProperty]
        public DateTimeOffset DateFrom { get; set; } = DateTimeOffset.Now.AddDays(-30);
        [BindProperty]
        public DateTimeOffset DateTo { get; set; } = DateTimeOffset.Now;

        public int TweetCount { get; set; }
        public void OnGet()
        {
            
        }

        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                return Page();
            }

            string consumerKey = "MmiVY1qtW6NKXEUqDMIhxH7Zk";
            string consumerSecret = "9uVYrtEtdmZiAzUFNqPyj3eU2uFyUUiUPeHde6zcWgWsCKiqI8";
            string accessToken = "25368429-RIo1mxKU0vDl5fwgdkzjUr3KexrkpuasuCFC4809J";
            string accessSecret = "2lKjkdBuTziqLAJ1jKJp5fyQwAIoiZVY6KqEC1QuAKo3M";

            var userClient = new TwitterClient(consumerKey, consumerSecret, accessToken, accessSecret);

            var userTimelineIterator = userClient.Timelines.GetUserTimelineIterator(TwitterId);
            var tweetsList = new List<TweetModel>();

            while (!userTimelineIterator.Completed)
            {
                var page = await userTimelineIterator.NextPageAsync();
                var tweets = page.Where(a => a.CreatedAt >= DateFrom && a.CreatedAt < DateTo.AddDays(1)).Select(a => a);
                foreach (var tweet in tweets)
                {
                    tweetsList.Add(
                        new TweetModel
                        {
                            Id = tweet.IdStr,
                            Text = tweet.FullText,
                            RetweetCount = tweet.RetweetCount,
                            FavoriteCount = tweet.FavoriteCount,
                            DateTime = tweet.CreatedAt.ToString(),
                            Hashtags = String.Join(",", tweet.Hashtags),
                            IsRetweet = tweet.IsRetweet,
                            IsQuote = tweet.QuotedTweet != null,
                            Mention = String.Join(",", tweet.UserMentions)
                        });
                }
                TweetCount += page.Count();
                break;
            }

            var file = SaveToCSV(tweetsList);
            if (!string.IsNullOrEmpty(file))
            {
                var dt = DateTime.Now;
                Response.Headers.Add("content-disposition", "inline;filename=" + $"{TwitterId}-{dt.ToShortDateString()}-{dt.ToShortTimeString()}.csv");
                return Content(file, "text/csv", Encoding.UTF8);
            }

            return Page();
        }

        private string SaveToCSV(List<TweetModel> tweets)
        {
            var result = "";
            using (var mem = new MemoryStream())
            using (var writer = new StreamWriter(mem))
            using (var csv = new CsvWriter(writer, CultureInfo.InvariantCulture))
            {
                csv.WriteRecords(tweets);

                csv.WriteHeader<TweetModel>();
                csv.WriteRecords(TweetsList);

                writer.Flush();
                result = Encoding.UTF8.GetString(mem.ToArray());
            }
            //return result;
            return result;
        }
    }
}