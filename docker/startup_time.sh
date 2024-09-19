START=$(date +%s)
docker build -t contact-mgmt-system:1.0.0 .
docker run -d -p 5000:5000 contact-mgmt-system:1.0.0
until curl -s http://127.0.0.1:5000 > /dev/null; do
  sleep 0.1
done
END=$(date +%s)
echo "Startup time: $((END - START)) seconds"