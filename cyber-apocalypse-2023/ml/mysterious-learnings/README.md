# mysterious-learnings

**SOLVED**

> One day the archeologist came across a strange metal plate covered in uncommon hieroglyphics. 
> It looked like blueprints for some kind of alien technology. 
> "What kind of magic is this?" He studied the plate more closely and was amazed by the advanced technology and incredible engineering they were using at a time like this. 
> This could only lead him in him wanting to learn more...

h5 file? looks like its storing a model with some weights/biases 

`strings alien.h5 | less`

tensorflow

https://naadispeaks.wordpress.com/2021/06/30/using-hierarchical-data-format-hdf5-in-machine-learning/

https://www.tensorflow.org/install/pip

```sh
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

source ~/.zshrc
conda create --name tf python=3.9
# conda deactivate
conda activate tf

pip3 install numpy --upgrade
pip3 install tensorflow

conda install cudatoolkit
conda install cudnn
export LD_LIBRARY_PATH=/usr/local/lib
sudo apt install nvidia-cuda-toolkit

# verify cpu
python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```

https://www.hdfgroup.org

`strings | alien.h5`

4wEAAAAAAAAAAAAAAAEAAAABAAAAQwAAAHMEAAAAfABTACkBTqkAKQHaAXhyAQAAAHIBAAAA+h88\naXB5dGhvbi1pbnB1dC0xMi02ZGI4ZTVhZTA2ZGE+2gg8bGFtYmRhPggAAADzAAAAAA==

4wEAAAAAAAAAAAAAAAEAAAACAAAAQwAAAHMMAAAAdABkAYMBAQB8AFMAKQJO2g1TRlJDZTI0d2RG\nOXpiKQHaBXByaW50KQHaAXipAHIEAAAA+h88aXB5dGhvbi1pbnB1dC0xMS1kNTY5YzRhOTUyYjQ+\n2gltYWxpY2lvdXMCAAAAcwQAAAAAAQgB


see `model_config.json`

```json
{
    "layers": [
        {
            "class_name": "InputLayer",
            "config": {
                "batch_input_shape": [
                    null,
                    32,
                    32,
                    3
                ],
                "dtype": "float32",
                "sparse": false,
                "ragged": false,
                "name": "conv2d_3_input"
            }
        }
    ]
}
```


strange data? encoded?

19oNHJkX3RvX3V
4wEAAAAAAAAAAAAAAAEAAAABAAAAQwAAAHMEAAAAfABTACkBTqkAKQHaAXhyAQAAAHIBAAAA+h88\naXB5dGhvbi1pbnB1dC0xMi02ZGI4ZTVhZTA2ZGE+2gg8bGFtYmRhPggAAADzAAAAAA==\n
4wEAAAAAAAAAAAAAAAEAAAACAAAAQwAAAHMMAAAAdABkAYMBAQB8AFMAKQJO2g1TRlJDZTI0d2RG\nOXpiKQHaBXByaW50KQHaAXipAHIEAAAA+h88aXB5dGhvbi1pbnB1dC0xMS1kNTY5YzRhOTUyYjQ+\n2gltYWxpY2lvdXMCAAAAcwQAAAAAAQgB\n
SFRCe24wdF9zb



19oNHJkX3RvX3V
4wEAAAAAAAAAAAAAAAEAAAABAAAAQwAAAHMEAAAAfABTACkBTqkAKQHaAXhyAQAAAHIBAAAA+
h88aXB5dGhvbi1pbnB1dC0xMi02ZGI4ZTVhZTA2ZGE+
2gg8bGFtYmRhPggAAADzAAAAAA==
4wEAAAAAAAAAAAAAAAEAAAACAAAAQwAAAHMMAAAAdABkAYMBAQB8AFMAKQJO2g1TRlJDZTI0d2RG
OXpiKQHaBXByaW50KQHaAXipAHIEAAAA+h88aXB5dGhvbi1pbnB1dC0xMS1kNTY5YzRhOTUyYjQ+
2gltYWxpY2lvdXMCAAAAcwQAAAAAAQgB
SFRCe24wdF9zb
uZDNyc3Q0bmR9


aXB5dGhvbi1pbnB1dC0xMi02ZGI4ZTVhZTA2ZGE                     -> ipython-input-12-6db8e5ae06da
2gltYWxpY2lvdXMCAAAAcwQAAAAAAQgBSFRCe24wdF9zb               -> Ú	malicious....s........HTB{n0t_s
2gltYWxpY2lvdXMCAAAAcwQAAAAAAQgBSFRCe24wdF9zb19oNHJkX3RvX3V -> malicious....s........HTB{n0t_so_h4rd_to_u

2gltYWxpY2lvdXMCAAAAcwQAAAAAAQgBSFRCe24wdF9zb19oNHJkX3RvX3V

2gltYWxpY2lvdXMCAAAAcwQAAAAAAQgBSFRCe24wdF9zb19oNHJkX3RvX3V

SFRCe24wdF9zb19oNHJkX3RvX3V -> HTB{n0t_so_h4rd_to_u

SFRCe24wdF9zb19oNHJkX3RvX3VuZDNyc3Q0bmR9 -> `HTB{n0t_so_h4rd_to_und3rst4nd}`