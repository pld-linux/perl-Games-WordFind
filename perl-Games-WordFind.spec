%include	/usr/lib/rpm/macros.perl
%define	pdir	Games
%define	pnam	WordFind
Summary:	Games::WordFind perl module
Summary(pl):	Modu³ perla Games::WordFind
Name:		perl-Games-WordFind
Version:	0.02
Release:	9
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

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README examples
%{perl_sitelib}/Games/WordFind.pm
%dir %{perl_sitelib}/auto/Games/WordFind
%{perl_sitelib}/auto/Games/WordFind/autosplit.ix
%{_mandir}/man3/*
