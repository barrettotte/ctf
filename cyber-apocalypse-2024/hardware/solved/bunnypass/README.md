# bunnypass

As you discovered in the PDF, the production factory of the game is revealed. This factory manufactures all the hardware devices and custom silicon chips (of common components) that The Fray uses to create sensors, drones, and various other items for the games. Upon arriving at the factory, you scan the networks and come across a RabbitMQ instance. It appears that default credentials will work.

## Solution

83.136.254.108:38824

```sh
nc 83.136.254.108 38824
```

rabbitmq default creds: guest/guest

Queues - `factory_idle`, fetched all messages, last one:

`HTB{th3_hunt3d_b3c0m3s_th3_hunt3r}`
