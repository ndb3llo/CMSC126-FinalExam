host="$1"
shift

if [ "$1" = "--" ]; then
  shift
fi

cmd="$@"

until nc -z "$host" 5432; do
  echo "Still waiting for $host..."
  sleep 1
done

echo "$host is up - executing command"
exec $cmd
