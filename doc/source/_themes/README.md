#G-Node Sphinx Styles

This repo is home to in-house [Sphinx](http://sphinx.pocoo.org) themes used by the [German INCF Node](http://www.g-node.org). Their basic design is derived from [Flask](http://flask.pocoo.org)'s documentation. If you want to use it in your projects, follow these steps:

1. Set up a git submodule in your documentation folder under '_themes' that
   checks out the contents of this repository, or copy the files by hand.
   
2. Adjust your conf.py as follows:

        sys.path.append(os.path.abspath('_themes'))
        html_theme_path = ['_themes']
        html_theme = 'gnode'

The following themes currently exist:

- _gnode_
- _gnode_small_ - Smaller version of the fully-fledged theme for one-page documentation.

Following Flask's themes, a number of options exist for _gnode_ themes:

    [options]
    index_logo = ''              filename of a picture in _static
                                 to be used as replacement for the
                                 h1 in the index.rst file.
    index_logo_height = 120px    height of the index logo
    github_fork = ''             repository name on github for the
                                 "fork me" badge
                              
__Acknowledgements__: Many thanks to Armin Ronacher for publishing and open-sourcing the templates.