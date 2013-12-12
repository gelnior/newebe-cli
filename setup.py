from setuptools import setup
import newebecli

setup(
    name='newebecli',
    version='0.1.0',
    description='CLI for Newebe',
    author='Gelnior',
    author_email='gelnior@free.fr',
    url='http://newebe.org/',
    license='BSD',
    install_requires=[
        "docopt==0.6.1",
        "requests>=2.0.0",
    ],
    setup_requires=[],
    tests_require=[
    ],
    packages=['newebecli'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'newebecli = newebecli.__main__:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GPL',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration',
    ],
)
