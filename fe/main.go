package main

import (
	"net/http"
)

func main() {
	http.Handle("/",
		http.FileServer(http.Dir("dist")))
	http.Handle("/maps/",
		http.StripPrefix("/maps", http.FileServer(http.Dir("src/assets/maps"))))
	http.ListenAndServe(":1337", nil)
}