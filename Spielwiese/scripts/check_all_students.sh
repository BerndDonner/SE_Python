#!/usr/bin/env bash
set -euo pipefail

BASE_BRANCH="${1:-master}"

# Liste der Schüler-Logins/Branches hier eintragen:
STUDENTS=(
  "ThomasBomber"
  "Goaslschnoizer"
  "Uebung12_11"
  # weitere Logins/Branches hier ergänzen ...
)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHECK_SCRIPT="$SCRIPT_DIR/check_student_branch.sh"

if [ ! -x "$CHECK_SCRIPT" ]; then
  echo "❌ $CHECK_SCRIPT not found or not executable." >&2
  exit 1
fi

echo "📦 Base branch for all checks: $BASE_BRANCH"
echo

FAILED=()

for student in "${STUDENTS[@]}"; do
  BRANCH="$student"   # falls Branchname != Login ist, hier anpassen

  echo "==============================="
  echo "🔍 Checking student: $student"
  echo "   Branch:          $BRANCH"
  echo "==============================="

  if git rev-parse --verify "$BRANCH" >/dev/null 2>&1; then
    if "$CHECK_SCRIPT" "$BASE_BRANCH" "$BRANCH" "$student"; then
      echo "✅ OK for $student"
    else
      echo "❌ VIOLATIONS for $student"
      FAILED+=("$student")
    fi
  else
    echo "⚠️ Branch '$BRANCH' does not exist – skipping."
  fi

  echo
done

if [ "${#FAILED[@]}" -gt 0 ]; then
  echo "❌ Some students have disallowed changes:"
  for s in "${FAILED[@]}"; do
    echo "   - $s"
  done
  exit 1
fi

echo "✅ All checked student branches are structurally safe for fast-forward into $BASE_BRANCH."
