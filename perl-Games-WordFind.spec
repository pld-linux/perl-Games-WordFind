%define	pdir	Games
%define	pnam	WordFind
%include	/usr/lib/rpm/macros.perl
Summary:	Games-WordFind perl module
Summary(pl):	Modu³ perla Games-WordFind
Name:		perl-Games-WordFind
Version:	0.02
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Games-WordFind module simply provides a class which can be used to
generate WordFind type puzzles.

%description -l pl
Games-WordFind udostêpnia klasê do generowania puzzli.

%prep
%setup -q -n Games-WordFind-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz examples
%{perl_sitelib}/Games/WordFind.pm
%{perl_sitelib}/auto/Games/WordFind/autosplit.ix
%{_mandir}/man3/*
