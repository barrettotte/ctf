# packed-away

To escape the arena's latest trap, you'll need to get into a secure vault - and quick! There's a password prompt waiting for you in front of the door however - can you unpack the password quick and get to safety?

## Solution

```sh
strings packed | less

# Hr3t_0f_th3_p45}
# $Info: This file is packed with the UPX executable packer http://upx.sf.net

```

https://www.youtube.com/watch?v=0jVikfySiII

```sh
# https://github.com/upx/upx/releases/tag/v4.2.2

~/Downloads/upx-4.2.2-amd64_linux/upx -d packed

strings packed | less
# HTB{unp4ck3dr3t_HH0f_th3_pH0f_th3_pH0f_th3_pH0f_th3_pH
# HTB{unp4ck3d_th3_s3cr3t_0f_th3_p455w0rd}

```

