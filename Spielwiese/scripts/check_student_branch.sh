#!/usr/bin/env bash
set -euo pipefail

# Simple helper to print usage information
usage() {
  echo "Usage: $0 <base-branch> <student-branch> <student-login>" >&2
  echo "Example: $0 master ThomasBomber ThomasBomber" >&2
  exit 1
}

BASE_BRANCH="${1:-}"
STUDENT_BRANCH="${2:-}"
ACTOR="${3:-}"

if [ -z "$BASE_BRANCH" ] || [ -z "$STUDENT_BRANCH" ] || [ -z "$ACTOR" ]; then
  usage
fi

# Check that we are in a git repository
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "❌ This is not a git repository." >&2
  exit 1
fi

# Check that branches exist
if ! git rev-parse --verify "$BASE_BRANCH" >/dev/null 2>&1; then
  echo "❌ Base branch '$BASE_BRANCH' does not exist." >&2
  exit 1
fi

if ! git rev-parse --verify "$STUDENT_BRANCH" >/dev/null 2>&1; then
  echo "❌ Student branch '$STUDENT_BRANCH' does not exist." >&2
  exit 1
fi

echo "📦 Base branch:    $BASE_BRANCH"
echo "📦 Student branch: $STUDENT_BRANCH"
echo "👤 Student login:  $ACTOR"
echo

# Escape regex special chars in actor name (just in case)
ACTOR_ESCAPED=$(printf '%s\n' "$ACTOR" | sed 's/[][(){}.^$+*?|\\/]/\\&/g')

# Compute diff between base and student branch as one big change set.
# --no-renames: treat renames as delete+add so source paths show up.
CHANGED=$(git -c core.quotepath=off diff --no-renames --name-only \
  "${BASE_BRANCH}..${STUDENT_BRANCH}")

echo "📄 Paths changed between ${BASE_BRANCH} and ${STUDENT_BRANCH}:"
if [ -z "$CHANGED" ]; then
  echo "(no changes)"
  echo
else
  echo "$CHANGED"
  echo
fi

# If there are no changes at all, we are trivially fine
if [ -z "$CHANGED" ]; then
  echo "✅ No changes – merge is structurally safe."
  exit 0
fi

# Allowed prefixes:
#   <ACTOR>/      -> student's own directory
#   common/       -> shared stuff (optional, remove if you don't want that)
#   shared/       -> another shared directory (optional)
#   README.md     -> top-level README
#   $             -> empty lines (safety)
ALLOWED_REGEX="^(${ACTOR_ESCAPED}/|common/|shared/|README\.md|$)"

echo "🧩 Allowed path prefixes (regex): $ALLOWED_REGEX"
echo

# Filter out everything that does NOT match the allowed prefixes
VIOLATIONS=$(printf '%s\n' "$CHANGED" | grep -Ev "$ALLOWED_REGEX" || true)

if [ -n "$VIOLATIONS" ]; then
  echo "❌ Found disallowed paths in diff ${BASE_BRANCH}..${STUDENT_BRANCH}:"
  echo "$VIOLATIONS"
  echo
  echo "💡 Only changes under '${ACTOR}/' (and common/, shared/, README.md) are allowed."
  exit 1
fi

echo "✅ All changes between ${BASE_BRANCH} and ${STUDENT_BRANCH} are within:"
echo "   - ${ACTOR}/"
echo "   - common/, shared/, README.md (if present)"
echo "👉 Fast-forward merge should be structurally safe."
