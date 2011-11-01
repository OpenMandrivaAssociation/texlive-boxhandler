Name:		texlive-boxhandler
Version:	1.22
Release:	1
Summary:	Flexible Captioning and Deferred Box/List Printing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/boxhandler
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boxhandler.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boxhandler.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boxhandler.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package allows the user to optimise presentation of LaTeX
tables and figures. Boxhandler will lay out table and figure
captions with a variety of stylistic apperances, and will also
allow figures and tables to be "wrapped" in a manner consistent
with many business and government documents. For a document
that might appear in different venues with different
formatting, boxhandler permits the creation of a LaTeX source
document that can, with a single-line change in the source
code, produce an output that has very different layout from the
baseline configuration, not only in terms of caption style, but
more importantly in terms of the locations where figures,
tables and lists appear (or not) in the document. Deferral
routines also allow one to keep all figure and table data in a
separate source file, while nonetheless producing a document
with figures and tables appearing in the desired location.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/boxhandler/boxhandler.sty
%doc %{_texmfdistdir}/doc/latex/boxhandler/README
%doc %{_texmfdistdir}/doc/latex/boxhandler/boxhandler.pdf
#- source
%doc %{_texmfdistdir}/source/latex/boxhandler/boxhandler.dtx
%doc %{_texmfdistdir}/source/latex/boxhandler/boxhandler.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
