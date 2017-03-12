
#!/bin/bash
echo "Copying preparenode.sh to nodes"
pscp -v -l root -h hosts.txt -x " -oStrictHostKeyChecking=no" preparenode.sh /root/preparenode.sh

echo "Starting preparenode.sh on each node"
pssh -v -t 0 -l root -h hosts.txt -x "-t -t -oStrictHostKeyChecking=no" 'chmod u+x preparenode.sh && ./preparenode.sh >> preparenode.log && sudo reboot'
