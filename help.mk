# This Makefile uses an auto generated help message with categories
# To include a target in the help message, just start the comment with ##
# To specify a category use @
# See an example below.
RED  := $(shell tput -Txterm setaf 1)
GREEN  := $(shell tput -Txterm setaf 2)
WHITE  := $(shell tput -Txterm setaf 7)
YELLOW := $(shell tput -Txterm setaf 3)
BLUE := $(shell tput -Txterm setaf 4)
RESET  := $(shell tput -Txterm sgr0)
HELP_FUNC = \
	%help; \
	while(<>) { push @{$$help{$$2 // 'Others'}}, [$$1, $$3] if /^([a-zA-Z\-\_.\[\]]+)\s*:.*\#\#(?:@([a-zA-Z\-\.\[\]]+))?\s(.*)$$/ }; \
	print "usage: make [target]\n\n"; \
	for (sort keys %help) { \
		print "${WHITE}$$_:${RESET}\n"; \
		for (@{$$help{$$_}}) { \
			$$sep = "·" x (42 - length $$_->[0]); \
			print "  ${YELLOW}$$_->[0]${BLUE}$$sep${GREEN}$$_->[1]${RESET}\n"; \
		}; \
		print "\n"; \
	}
help: ##@Basic Print this help message
	@perl -e '$(HELP_FUNC)' $(MAKEFILE_LIST)
