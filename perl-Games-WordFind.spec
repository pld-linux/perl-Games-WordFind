#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Games
%define		pnam	WordFind
Summary:	Games::WordFind - class for generating "word find" type puzzles
Summary(pl.UTF-8):	Games::WordFind - klasa do generowania układanek słownych
Name:		perl-Games-WordFind
Version:	0.02
Release:	15
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	28bfa49532f2a49fd455fbd3b9afeb9e
URL:		http://search.cpan.org/dist/Games-WordFind/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Games::WordFind Perl module simply provides a class which can be used
to generate "word find" type puzzles.

%description -l pl.UTF-8
Games::WordFind udostępnia klasę do generowania układanek słownych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Games/WordFind.pm
%dir %{perl_vendorlib}/auto/Games
# empty autosplit.ix
#%dir %{perl_vendorlib}/auto/Games/WordFind
#%%{perl_vendorlib}/auto/Games/WordFind/autosplit.ix
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
