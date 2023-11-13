%% royalty
mother(charles, elizabeth).
mother(anne, elizabeth).
mother(andrew, elizabeth).
mother(edward, elizabeth).
mother(william, diana).
mother(harry, diana).
mother(george, catherine).
mother(charlotte, catherine).
mother(louis, catherine).
mother(archie, meghan).
father(charles, philip).
father(anne, philip).
father(andrew, philip).
father(edward, philip).
father(william, charles).
father(harry, charles).
father(george, william).
father(charlotte, william).
father(louis, william).
father(archie, harry).

siblings(elizabeth, margaret).
siblings(X, Y) :- mother(X, M), father(X, F), mother(Y, M), father(Y, F), not(X = Y).

spouse(sarah, andrew).
spouse(sophie, edward).
spouse(Wife, Husband) :- mother(C, Wife), father(C, Husband).

%% independent predicates
parent(Child, Parent) :- mother(Child, Parent); father(Child, Parent).
aunt_or_uncle(Nephew, X) :- 
	parent(Nephew, P), siblings(P, X); 
	parent(Nephew, P), siblings(P, Y), spouse(Y, X); 
	parent(Nephew, P), siblings(P, Y), spouse(X, Y).
cousin(X, Y) :- parent(X, P), siblings(P, S), parent(Y, S).

%% queries
%% 	findall(X, siblings(louis, X), LS).       %% siblings of louis: [george, charlotte]
%%	findall(X, parent(louis, X), LP).         %% parents of louis: [catherine, william]
%%	findall(X, cousin(archie, X), AC).        %% cousins of archie: [george, charlotte, louis]
%%	findall(X, aunt_or_uncle(archie, X), AU). %% uncles & aunts of archie: [william, catherine]
%%	findall(X, aunt_or_uncle(X, anne), UA).   %% nephews of anne: [william, harry]