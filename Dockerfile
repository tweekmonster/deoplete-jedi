FROM zchee/neovim-python
MAINTAINER zchee <k@zchee.io>

RUN pip install jedi \
	&& pip3 install jedi \
	&& git clone https://github.com/Shougo/deoplete.nvim \
	&& git clone https://github.com/Shougo/neco-syntax \
	&& git clone https://github.com/Shougo/neoinclude.vim

WORKDIR /root/.config/nvim
