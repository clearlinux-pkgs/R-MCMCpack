#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-MCMCpack
Version  : 1.4.4
Release  : 18
URL      : https://cran.r-project.org/src/contrib/MCMCpack_1.4-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/MCMCpack_1.4-4.tar.gz
Summary  : Markov Chain Monte Carlo (MCMC) Package
Group    : Development/Tools
License  : GPL-3.0
Requires: R-MCMCpack-lib = %{version}-%{release}
BuildRequires : R-MatrixModels
BuildRequires : R-SparseM
BuildRequires : R-coda
BuildRequires : R-mcmc
BuildRequires : R-quantreg
BuildRequires : buildreq-R

%description
/////////////////////
/////////////////////
// Authors
Andrew D. Martin <admart@umich.edu>
Kevin M. Quinn <kmq@umich.edu>
Jong Hee Park <jongheepark@snu.ac.kr>

%package lib
Summary: lib components for the R-MCMCpack package.
Group: Libraries

%description lib
lib components for the R-MCMCpack package.


%prep
%setup -q -c -n MCMCpack

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552885221

%install
export SOURCE_DATE_EPOCH=1552885221
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MCMCpack
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MCMCpack
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MCMCpack
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  MCMCpack || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/MCMCpack/CITATION
/usr/lib64/R/library/MCMCpack/DESCRIPTION
/usr/lib64/R/library/MCMCpack/HISTORY
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
