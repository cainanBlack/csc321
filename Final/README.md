#This is my final project for Network Management

This is code that tracks the communication between two docker containers and sniffs thier packets


The .py files are used for the initial communication of the docker container.


The first .pcap files are the inital files, to get these I used:
```
tcpdump -i any -w 'filename.pcap'
```

The files ending in "P.pcap" are the parsed files. To parse the files, I used:
```
tcpdump -n -r and specified the port to parse out all the excess information
```

Then the parsed files were combined into weather.pcap and task.pcap using mergecap:
```
mergecap -w weather.pcap wuserverP.pcap wuclientP.pcap
mergecap -w task.pcap tasksinkP.pcap taskventP.pcap taskworkP.pcap
```

To combine all of my files into finalP.pcap, I used:
```
mergecap -final.pcap weather.pcap task.pcap
```
