#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Games
%define		pnam	WordFind
Summary:	Games::WordFind Perl module
Summary(cs):	Modul Games::WordFind pro Perl
Summary(da):	Perlmodul Games::WordFind
Summary(de):	Games::WordFind Perl Modul
Summary(es):	Módulo de Perl Games::WordFind
Summary(fr):	Module Perl Games::WordFind
Summary(it):	Modulo di Perl Games::WordFind
Summary(ja):	Games::WordFind Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Games::WordFind ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Games::WordFind
Summary(pl):	Modu³ Perla Games::WordFind
Summary(pt):	Módulo de Perl Games::WordFind
Summary(pt_BR):	Módulo Perl Games::WordFind
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Games::WordFind
Summary(sv):	Games::WordFind Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Games::WordFind
Summary(zh_CN):	Games::WordFind Perl Ä£¿é
Name:		perl-Games-WordFind
Version:	0.02
Release:	12
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Games::WordFind module simply provides a class which can be used to
generate WordFind type puzzles.

%description -l pl
Games::WordFind udostêpnia klasê do generowania uk³adanek s³ownych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Games/WordFind.pm
%dir %{perl_sitelib}/auto/Games
# empty autosplit.ix
#%dir %{perl_sitelib}/auto/Games/WordFind
#%{perl_sitelib}/auto/Games/WordFind/autosplit.ix
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
