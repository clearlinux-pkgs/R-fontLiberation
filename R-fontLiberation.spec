#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fontLiberation
Version  : 0.1.0
Release  : 32
URL      : https://cran.r-project.org/src/contrib/fontLiberation_0.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fontLiberation_0.1.0.tar.gz
Summary  : Liberation Fonts
Group    : Development/Tools
License  : OFL-1.1
BuildRequires : buildreq-R

%description
`fontquiver` package. This fontset covers the 12 combinations of
    families (sans, serif, mono) and faces (plain, bold, italic, bold
    italic) supported in R graphics devices.

%prep
%setup -q -c -n fontLiberation
cd %{_builddir}/fontLiberation

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641018747

%install
export SOURCE_DATE_EPOCH=1641018747
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fontLiberation
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fontLiberation
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fontLiberation
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fontLiberation || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fontLiberation/DESCRIPTION
/usr/lib64/R/library/fontLiberation/LICENSE
/usr/lib64/R/library/fontLiberation/Meta/Rd.rds
/usr/lib64/R/library/fontLiberation/Meta/features.rds
/usr/lib64/R/library/fontLiberation/Meta/hsearch.rds
/usr/lib64/R/library/fontLiberation/Meta/links.rds
/usr/lib64/R/library/fontLiberation/Meta/nsInfo.rds
/usr/lib64/R/library/fontLiberation/Meta/package.rds
/usr/lib64/R/library/fontLiberation/NAMESPACE
/usr/lib64/R/library/fontLiberation/fonts/Makefile
/usr/lib64/R/library/fontLiberation/fonts/liberation-VERSION
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/AUTHORS
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/ChangeLog
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LICENSE
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationMono-Bold.ttf
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationMono-Bold.woff
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationMono-BoldItalic.ttf
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationMono-BoldItalic.woff
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationMono-Italic.ttf
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationMono-Italic.woff
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationMono-Regular.ttf
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationMono-Regular.woff
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSans-Bold.ttf
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSans-Bold.woff
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSans-BoldItalic.ttf
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSans-BoldItalic.woff
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSans-Italic.ttf
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSans-Italic.woff
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSans-Regular.ttf
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSans-Regular.woff
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSerif-Bold.ttf
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSerif-Bold.woff
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSerif-BoldItalic.ttf
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSerif-BoldItalic.woff
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSerif-Italic.ttf
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSerif-Italic.woff
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSerif-Regular.ttf
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/LiberationSerif-Regular.woff
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/README
/usr/lib64/R/library/fontLiberation/fonts/liberation-fonts/TODO
/usr/lib64/R/library/fontLiberation/help/AnIndex
/usr/lib64/R/library/fontLiberation/help/aliases.rds
/usr/lib64/R/library/fontLiberation/help/fontLiberation.rdb
/usr/lib64/R/library/fontLiberation/help/fontLiberation.rdx
/usr/lib64/R/library/fontLiberation/help/paths.rds
/usr/lib64/R/library/fontLiberation/html/00Index.html
/usr/lib64/R/library/fontLiberation/html/R.css
