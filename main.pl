#!/usr/bin/perl
use strict;
use warnings;

use Champion;
use Summoner;
use Matchhistory;
use Stats;
use League;

print "Enter your summoner name: ";
my $name = <STDIN>;
chomp($name);

my $summoner = Summoner::by_name($name);
my $sumId = $summoner->{"id"};
my $league = League::league($sumId);
my $matchhistory = Matchhistory::matchhistory($sumId);
my $stats = Stats::stats($sumId);

print $name,"\n";
print "-" x 25;
print "\n";

printf ("TIER: %s\nDIVISION: %s\n\n",$league->{"tier"}, $league->{"division"});
printf ("GAMES PLAYED: %d\nWINS: %d\nLOSSES: %d\nTOTAL KDA: %d/%d/%d\n", $stats->{0}->{"totalSessionsPlayed"}, $stats->{0}->{"totalSessionsWon"}, $stats->{0}->{"totalSessionsLost"}, $stats->{0}->{"totalChampionKills"}, $stats->{0}->{"totalDeathsPerSession"}, $stats->{0}->{"totalAssists"});
print "-" x 25;
print "\n";

printf ("Top     - %dG %dW %dL\n",$matchhistory->{"totalTop"},     $matchhistory->{"topWins"},     $matchhistory->{"totalTop"} -     $matchhistory->{"topWins"});
printf ("Jungle  - %dG %dW %dL\n",$matchhistory->{"totalJG"},      $matchhistory->{"jgWins"},      $matchhistory->{"totalJG"} -      $matchhistory->{"jgWins"});
printf ("Middle  - %dG %dW %dL\n",$matchhistory->{"totalMid"},     $matchhistory->{"midWins"},     $matchhistory->{"totalMid"} -     $matchhistory->{"midWins"});
printf ("ADC     - %dG %dW %dL\n",$matchhistory->{"totalADC"},     $matchhistory->{"adcWins"}, 	   $matchhistory->{"totalADC"} -     $matchhistory->{"adcWins"});
printf ("Support - %dG %dW %dL\n",$matchhistory->{"totalSupport"}, $matchhistory->{"supportWins"}, $matchhistory->{"totalSupport"} - $matchhistory->{"supportWins"});
print "-" x 25;
print "\n";

for (my $i = 1; $i < ($matchhistory->{"totalGamesPlayed"}) + 1; $i++){
	my $id         = $matchhistory->{"championData"}->{$i}->{"id"};
	my $kills      = $matchhistory->{"championData"}->{$i}->{"kills"};
	my $deaths     = $matchhistory->{"championData"}->{$i}->{"deaths"};
	my $assists    = $matchhistory->{"championData"}->{$i}->{"assists"};
	my $creepScore = $matchhistory->{"championData"}->{$i}->{"creepScore"};
	my $outcome    = $matchhistory->{"championData"}->{$i}->{"outcome"};
	my $champion = Champion::champion($id);
	my $role = $matchhistory->{"championData"}->{$i}->{"role"};
	
	if ($outcome eq "true"){
		$outcome = "WIN";
	}elsif ($outcome eq "false"){
		$outcome = "LOST";
	}
	printf ("%d. %s \@ %s\nCHAMPION: %s\nKDA: %d/%d/%d\nCS: %d\n", $i, $outcome, $role, $champion, $kills, $deaths, $assists, $creepScore);
	print "-" x 10;
	print "\n";
}