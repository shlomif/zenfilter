from setuptools import setup

setup(name='zenfilter',
        version='0.1a',
        description='Filters TravisCI output',
        author='Trashlord',
        author_email='dornenreich666@gmail.com',
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


