# CONTRIBUTING #

### Bugs?

* Submit an issue on the [Issues page](https://github.com/sckott/pytaxa/issues)

### Issues and Pull Requests

If you are considering a pull request, you may want to open an issue first to discuss with the maintainer(s).

### Code contributions

* Fork this repo to your GitHub account
* Clone your version on your account down to your machine from your account, e.g,. `git clone https://github.com/<yourgithubusername>/pytaxa.git`
* Make sure to track progress upstream (i.e., on our version of `pytaxa` at `sckott/pytaxa`) by doing `git remote add upstream https://github.com/sckott/pytaxa.git`. Before making changes make sure to pull changes in from upstream by doing either `git fetch upstream` then merge later or `git pull upstream` to fetch and merge in one step
* Make your changes (bonus points for making changes on a new feature branch - see <https://guides.github.com/introduction/flow/> for how to contribute by branching, making changes, then submitting a pull request)
* Push up to your account
* Submit a pull request to home base (likely master branch, but check to make sure) at `sckott/pytaxa`

### Tests

If you are adding new features, or changing `pytaxa` functionality, make sure to run tests and add any tests as needed. We use [pytest]. Running tests should be as easy as `make test`.  

[pytest]: https://docs.pytest.org/en/latest/
