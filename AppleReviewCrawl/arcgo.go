package main

import (
    "fmt"
    //"net/http"
    //"strings"
    "flag"
)

type Review struct {
    name string
    content string
    score int
}

func crawl(id int) {
    url := fmt.Sprintf(`https://itunes.apple.com/rss/customerreviews/` +
        `page=1/id=%d` +
        `/sortby=mostrecent/json?l=en&&cc=cn`,
        id)
    body, err := http.Get(url)
    if err != nil {
        panic(err)
    }


}

func main() {
    var app_id int
    flag.IntVar(&app_id, "id", 0, "Apple App ID")
    flag.Parse()

    fmt.Printf("Crawl %d\n", app_id)
    crawl()
}
