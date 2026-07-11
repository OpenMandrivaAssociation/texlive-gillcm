%global tl_name gillcm
%global tl_revision 19878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Alternative unslanted italic Computer Modern fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/gillcm
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gillcm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gillcm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a demonstration of the use of virtual fonts for unusual effects:
the package implements an old idea of Eric Gill. The package was written
for the author's talk at TUG 2010.

