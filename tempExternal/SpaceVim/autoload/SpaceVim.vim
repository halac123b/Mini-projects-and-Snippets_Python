scriptencoding utf-8

""
" @section Introduction, intro
" @stylized spacevim
" @library
" @order intro options config functions layers usage plugins api dev community faq roadmap changelog
" SpaceVim is a modular configuration of Vim and Neovim.
" It's inspired by spacemacs. It manages collections of plugins in layers,
" which help to collect related packages together to provide features.
" This approach helps keep the configuration organized and reduces
" overhead for the user by keeping them from having to think about
" what packages to install.

""
" @section Highlighted Features, features
" @parentsection intro
" 1. Modularization: Plugins are organized in @section(layers).
" 2. Compatible API: A series of @section(api) for Vim/Neovim.
" 3. Great documentation: Everything is documented in `:h SpaceVim`.
" 4. Better experience: Most of the core plugins have been rewritten using Lua.
" 5. Beautiful UI: The interface has been carefully designed.
" 6. Mnemonic key bindings: Key bindings are organized using mnemonic prefixes.
" 7. Lower the risk of RSI: Heavily using the `<Space>` key instead of modifiers.

""
" @section Update and Rollback, update-and-rollback
" @parentsection intro
" @subsection Update SpaceVim itself
" 
" There are several methods of updating the core files of SpaceVim.
" It is recommended to update the packages first; see the next section.
"
" 1. Automatic Updates
" 
" By default, this feature is disabled.
" It would slow down the startup of Vim/Neovim.
" If you like this feature,
" add the following to your custom configuration file.
" >
"   [options]
"     automatic_update = true
" <
" 
" SpaceVim will automatically check for a new version
" every startup. You have to restart Vim after updating.
" 
" 2. Updating from the SpaceVim Buffer
" 
" Users can use command `:SPUpdate SpaceVim` to update SpaceVim.
" This command will open a new buffer to show the process of updating.
" 
" 3. Updating Manually with git
" 
" For users who prefer to use the command line, they can use the following command
" in a terminal to update SpaceVim manually:
" >
"   git -C ~/.SpaceVim pull
" <
" 
" @subsection Update plugins
" 
" Use `:SPUpdate` command to update all the plugins and
" SpaceVim itself. After `:SPUpdate`, you can assign
" plugins need to be updated. Use `Tab` to complete
" plugin names after `:SPUpdate`.
" 
" @subsection Reinstall plugins
" 
" When a plugin has failed to update or is broken, Use the `:SPReinstall`
" command to reinstall the plugin. The plugin's name can be completed via the key binding `<Tab>`.
" 
" For example:
" >
"   :SPReinstall echodoc.vim
" <
" 