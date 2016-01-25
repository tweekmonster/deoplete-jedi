import neovim


@neovim.plugin
class DeopleteJedi(object):

    def __init__(self, vim):
        self.vim = vim
        self.vim.vars['deoplete#source#jedi#channel_id'] = self.vim.channel_id

    """ rpc_export """
    @neovim.rpc_export('deoplete_source_jedi_buffer')
    def deoplete_source_jedi_buffer(self):
        # source = '\n'.join(self.vim.current.buffer[:])
        row, column = self.vim.current.window.cursor
        source = ''
        for i, line in enumerate(self.vim.current.buffer):
            if i == row - 1:
                source += line[:column] + line[column:]
            else:
                source += line
            source += '\n'
        self.vim.vars['deoplete#source#jedi#buffer'] = source
