# testimonial

As the leader of the Revivalists you are determined to take down the KORP, you and the best of your faction's hackers have set out to deface the official KORP website to send them a message that the revolution is closing in.

## Solution

```sh
docker run -d -p 1337:1337 -p 50045:50045 testimonial


```

GET http://localhost:1337/?testimonial=test&customer=barrett

```go
// interesting...

func (c *Client) SendTestimonial(customer, testimonial string) error {
	ctx := context.Background()
	// Filter bad characters.
	for _, char := range []string{"/", "\\", ":", "*", "?", "\"", "<", ">", "|", "."} {
		customer = strings.ReplaceAll(customer, char, "")
	}

	_, err := c.SubmitTestimonial(ctx, &pb.TestimonialSubmission{Customer: customer, Testimonial: testimonial})
	return err
}
```

```
client.go Sendtestimonial()
grpc.go SubmitTestimonial()

there has to be a way to write arbitrary files...
```

TODO:
