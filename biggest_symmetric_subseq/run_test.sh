while :
do
  node BiggestSymmetricalSubstring.js > /tmp/node.tmp && cat /tmp/node.tmp|../console/algorithm/test
  sleep 1s
done
