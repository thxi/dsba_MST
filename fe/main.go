package main

import (
	"net/http"
	"os"
)

func main() {
	http.Handle("/",
		http.FileServer(http.Dir("dist")))
	http.Handle("/maps/",
		http.StripPrefix("/maps", http.FileServer(http.Dir("src/assets/maps"))))

	port := os.Getenv("PORT")
	if port == "" {
		port = "1337"
	}

	http.ListenAndServe(":"+port, nil)
}
