# revision 19878
# category Package
# catalog-ctan undef
# catalog-date 2010-08-11 13:58:09 +0200
# catalog-license other-free
# catalog-version 1.1
Name:		texlive-gillcm
Version:	1.1
Release:	2
Summary:	Alternative unslanted italic Computer Modern fonts
Group:		Publishing
URL:		http://tug.org/texlive
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gillcm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gillcm.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a demonstration of the use of virtual fonts for unusual
effects: the package implements an old idea of Eric Gill. The
package was written for the author's talk at TUG 2010.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/gillcm/cmg.map
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbiu7t.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbiu8c.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbiu8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbiu8t.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgm8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmiu7t.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmiu8c.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmiu8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmiu8t.tfm
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgbi7t.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgbi8c.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgbi8t.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgbiu7t.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgbiu8c.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgbiu8t.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgmi7t.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgmi8c.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgmi8t.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgmiu7t.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgmiu8c.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgmiu8t.vf
%{_texmfdistdir}/tex/latex/gillcm/gillcm.sty
%{_texmfdistdir}/tex/latex/gillcm/ot1cmg.fd
%{_texmfdistdir}/tex/latex/gillcm/t1cmg.fd
%{_texmfdistdir}/tex/latex/gillcm/ts1cmg.fd
%doc %{_texmfdistdir}/doc/latex/gillcm/README
%doc %{_texmfdistdir}/doc/latex/gillcm/gillcm.bib
%doc %{_texmfdistdir}/doc/latex/gillcm/gillcm.dtx
%doc %{_texmfdistdir}/doc/latex/gillcm/gillcm.ins
%doc %{_texmfdistdir}/doc/latex/gillcm/gillcm.pdf
%doc %{_texmfdistdir}/doc/latex/gillcm/sample.pdf
%doc %{_texmfdistdir}/doc/latex/gillcm/sample.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
