from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='facebook_wordcloud',
      version='0.1',
      description='A Python tool for generating a word cloud for a Facebook chat conversation.',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Multimedia :: Graphics :: Presentation'
      ],
      keywords='facebook chat word cloud generate',
      url='https://github.com/mjmeli/facebook-chat-word-cloud',
      author='Michael Meli',
      author_email='facebook_wordcloud@michaelmeli.com',
      license='MIT',
      packages=['facebook_wordcloud'],
      install_requires=[
          'wordcloud',
          'python-dateutil',
          'lxml',
          'Pillow',
          'numpy'
      ],
      zip_safe=False,
      entry_points = {
          'console_scripts': ['facebook_wordcloud=facebook_wordcloud.command_line:main'],
      },
      test_suite='nose.collector',
      tests_require=['nose', 'mock'],
      include_package_data=True
)
