while :
do
  node solution.js > /tmp/node.tmp && cat /tmp/node.tmp|../console/algorithm/test
  sleep 1s
done
