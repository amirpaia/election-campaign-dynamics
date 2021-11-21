namespace Website.Models
{
    public class TweetModel
    {
        public string Id { get; set; }
        public string DateTime { get; set; }
        public int FavoriteCount { get; set; }
        public int RetweetCount { get; set; }
        public string Mention { get; set; }
        public bool IsRetweet { get; set; }
        public bool IsQuote { get; set; }
        public string Hashtags { get; set; }
        public string Text { get; set; }
    }
}
