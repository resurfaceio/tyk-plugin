FROM docker.tyk.io/tyk-gateway/tyk-gateway:v3.2.1
ENTRYPOINT [ "/bin/sh" ]
CMD ["-c", "/opt/tyk-gateway/tyk bundle build -y && rmdir tyk-*"]