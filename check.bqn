# used to verify what ytdl is downloading
CheckForFolderChangesForever ← {𝕊folder:
  {𝕊lines:
    •Delay 1
    nowLines ← •file.List folder
    {𝕊:
      •Show "Newone:"∾∾' '∾¨ 𝕩
    }⍟(⟨⟩⊸≢)lines (¬∘∊˜/⊢) nowLines
    nowLines
  }•_while_ 1 •file.List folder
}

# I found limits are (>⟜20∧<⟜9)changesToQualifyAsEqual currently
# No false positives found, 1 false negative found at 25.
CheckForDuplicates ← {changesToQualifyAsEqual𝕊files:
  n ← 2↕(".mp3"≡¯4↑⊢)¨⊸/∧𝕩
  (⍋•file.Created∘(folder⊸•file.At)¨)⊸⊏˘ n/˜15><∘(¯1⊑(1⊸+⥊+)○≠(⌊`⊢⌊⊏⊸»∘⊢-0∾1+⊣)˝=⌜⟜⌽)´˘ {𝕩↑¨˜⌈´≠¨𝕩}˘n
}

# Playlist folder
folder ← ".."

# Check for updates to playlist. Used to verify what ytdl is downloading, and what files it's creating. It makes a few temporary files.
#CheckForFolderChangesForever folder

# Show duplicates:
#•Out¨ 15 CheckForDuplicates •file.List folder

# Remove duplicates
# (Hopefully you have checked what will be deleted via above code)
#•file.Remove¨ folder⊸•file.At¨ ⊢˝⍉15 CheckForDuplicates •file.List folder
