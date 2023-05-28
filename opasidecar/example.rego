package example

import future.keywords.if

# デフォルトの拒否ルールを定義します
default allow := false

# alice は許可します
allow if input.user == "alice"