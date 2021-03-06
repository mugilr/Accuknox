package main

import (
    "fmt"
    "log"
    "time"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	now := time.Now()
	fmt.Println("The current datetime is:", now)
	fmt.Fprintf(w, "Welcome to GREAT KIRIKALAN MAGIC SHOW\n\n")
	ti := now.Format(time.Stamp)
	fmt.Fprintf(w, "Date & Time : %s \n\n", ti)
}

func main() {
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe(":8080", nil))
}
