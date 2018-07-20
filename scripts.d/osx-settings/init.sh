#!/bin/bash

# Install XCode command-line tools
xcode-select --install

# Dock: auto-hide
defaults write com.apple.dock autohide -bool true

# Dock: No delay before making Dock reappear
defaults write com.apple.Dock autohide-delay -float 0

# Finder: show status bar
defaults write com.apple.finder ShowStatusBar -bool true

# Finder: Show item info below desktop icons
/usr/libexec/PlistBuddy -c "Set :DesktopViewSettings:IconViewSettings:showItemInfo true" ~/Library/Preferences/com.apple.finder.plist

# Finder: Increase spacing between desktop icons
/usr/libexec/PlistBuddy -c "Set :DesktopViewSettings:IconViewSettings:gridSpacing 100" ~/Library/Preferences/com.apple.finder.plist

# Menu bar: show battery percentage
defaults write com.apple.menuextra.battery ShowPercent -string "YES"

# Menu bar: Show VPN menu
defaults write com.apple.systemuiserver menuExtras -array-add "/System/Library/CoreServices/Menu Extras/vpn.menu"

# Menu bar: Show date and day of week
defaults write com.apple.menuextra.clock DateFormat -string "EEE d MMM h:mm a"

###############################################################################
# Kill affected applications                                                  #
###############################################################################

for app in Finder Dock SystemUIServer; do
	killall "$app" > /dev/null 2>&1
done

echo "Done. Note that some of these changes might require a logout/restart to take effect."
