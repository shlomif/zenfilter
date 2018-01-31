from setuptools import setup

setup(
        name='zenfilter',
        version='0.4.0',
        description='Filters TravisCI output',
        author='Shlomi Fish',
        author_email='shlomif@shlomifish.org',
        license='MIT',
        keywords='travisci',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python :: 3'
            ],
        py_modules=['zenfilter'],
        entry_points={
            'console_scripts': [
                'zenfilter = zenfilter:zenfilter',
                ],
            },
)
