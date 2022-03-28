import nox

@nox.session(python=['3.7', '3.8', '3.9', '3.10', 'pypy3.7', 'pypy3.8', 'pypy3.9'])
def unittest(session):
    session.install('.[test]')
    session.run('pytest')
