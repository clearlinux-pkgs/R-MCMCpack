#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: 1eaf8cd
#
Name     : R-MCMCpack
Version  : 1.7.0
Release  : 60
URL      : https://cran.r-project.org/src/contrib/MCMCpack_1.7-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/MCMCpack_1.7-0.tar.gz
Summary  : Markov Chain Monte Carlo (MCMC) Package
Group    : Development/Tools
License  : GPL-3.0
Requires: R-MCMCpack-lib = %{version}-%{release}
Requires: R-coda
Requires: R-mcmc
Requires: R-quantreg
BuildRequires : R-coda
BuildRequires : R-mcmc
BuildRequires : R-quantreg
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
inference using posterior simulation for a number of
        statistical models. Most simulation is done in compiled C++
        written in the Scythe Statistical Library Version 1.0.3. All
        models return 'coda' mcmc objects that can then be summarized
        using the 'coda' package. Some useful
        utility functions such as density functions,
	pseudo-random number generators for statistical
        distributions, a general purpose Metropolis sampling algorithm,
        and tools for visualization are provided.

%package lib
Summary: lib components for the R-MCMCpack package.
Group: Libraries

%description lib
lib components for the R-MCMCpack package.


%prep
%setup -q -n MCMCpack
pushd ..
cp -a MCMCpack buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1705704390

%install
export SOURCE_DATE_EPOCH=1705704390
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/MCMCpack/CITATION
/usr/lib64/R/library/MCMCpack/DESCRIPTION
/usr/lib64/R/library/MCMCpack/HISTORY.txt
/usr/lib64/R/library/MCMCpack/INDEX
/usr/lib64/R/library/MCMCpack/Meta/Rd.rds
/usr/lib64/R/library/MCMCpack/Meta/data.rds
/usr/lib64/R/library/MCMCpack/Meta/features.rds
/usr/lib64/R/library/MCMCpack/Meta/hsearch.rds
/usr/lib64/R/library/MCMCpack/Meta/links.rds
/usr/lib64/R/library/MCMCpack/Meta/nsInfo.rds
/usr/lib64/R/library/MCMCpack/Meta/package.rds
/usr/lib64/R/library/MCMCpack/NAMESPACE
/usr/lib64/R/library/MCMCpack/R/MCMCpack
/usr/lib64/R/library/MCMCpack/R/MCMCpack.rdb
/usr/lib64/R/library/MCMCpack/R/MCMCpack.rdx
/usr/lib64/R/library/MCMCpack/data/Euro2016.rda
/usr/lib64/R/library/MCMCpack/data/Nethvote.rda
/usr/lib64/R/library/MCMCpack/data/PErisk.rda
/usr/lib64/R/library/MCMCpack/data/Rehnquist.rda
/usr/lib64/R/library/MCMCpack/data/Senate.rda
/usr/lib64/R/library/MCMCpack/data/SupremeCourt.rda
/usr/lib64/R/library/MCMCpack/help/AnIndex
/usr/lib64/R/library/MCMCpack/help/MCMCpack.rdb
/usr/lib64/R/library/MCMCpack/help/MCMCpack.rdx
/usr/lib64/R/library/MCMCpack/help/aliases.rds
/usr/lib64/R/library/MCMCpack/help/paths.rds
/usr/lib64/R/library/MCMCpack/html/00Index.html
/usr/lib64/R/library/MCMCpack/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/MCMCpack/libs/MCMCpack.so
/usr/lib64/R/library/MCMCpack/libs/MCMCpack.so.avx2
/usr/lib64/R/library/MCMCpack/libs/MCMCpack.so.avx512
