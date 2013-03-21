svn2rpm
=======
![Logo](https://raw.github.com/ImmobilienScout24/svn2rpm/master/svn2rpm-small.png)

Create RPM packages from SVN repository. The source files can be stored in 2 variants:

1. SPEC and SOURCES: Here we keep all the Source*: and Patch*: files together with the .spec file. If the Source*: and Patch*: keys contain URLS then svn2rpm will use spectool to download them.
2. SPEC and exploded Source: Here you must set "Source: %{name}-%{version}.tar.gz" and use %setup in your %build stage. In the %install stage you can then just copy the files/dirs into %{buildroot}.

The 2nd variant is especially useful for simple packages that just deploy a few files. The user sees the files in the SVN source location and only needs to write a few shell lines to put the files into the proper place. No hassle with packing archives, this is all abstracted away by svn2rpm.

Check out the stuff in test/data to see some examples for working spec files/configurations.

Usage
=====
```
svn2rpm 10.1.3
Export from SVN and build an SRC RPM package. Requirements:
- SPEC file must be part of files checked out from SVN
- VARIANT 1: SVN contains SPEC file and optionally SOURCES
- VARIANT 2: SVN is exploded SOURCE0

Usage:

svn2rpm [Options ...] <SVN URL|WORKING COPY PATH> [more rpmbuild parameters ...]

Options:
    -V          Version
    -h          Show help
    -s          Build only Source RPM
    -k          Keep work area (to debug RPM build issues)
    -d          Debug mode
    -b <tag>    Append tag to Release:
    -o <path>   Write resulting RPMs to path

Example:
svn2rpm <svn url> 
svn2rpm -b .is24 <working copy path>
svn2rpm <svn|wc> --define="key value"

Note: The RPM package name and version are taken from the SPEC file!!

For VARIANT 1 the sources will be downloaded with spectool.
```

TODO
====

* Add some tests
* Really detect the variant that is beeing used instead of trying both
* Better error reporting
