curl -X POST \
    -H "Accept: application/vnd.github.v3+json" \
    -H "Authorization: token ${GITHUB_TOKEN}" \
    --data '{"event_type": "aoc_timer", "client_payload": { "year": "2020", "day": "1"}}' \
    https://api.github.com/repos/hoxovic/aoc_timing/dispatches
