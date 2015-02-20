#!/usr/bin/perl
use strict;
use warnings;
use CGI qw/:standard/;

use Champion;
use Summoner;
use Matchhistory;
use Stats;
use League;

print "Content-type: text/html\n\n";
print start();
print main1();
print end();


sub start {
 return <<S;
<!DOTYPE html>
<html>
    <head>
        <title>lol\@myteam</title>
    </head>
    <body>
        <center><img src='banner.png' alt='lol\@myteam' height = '70px' width='450px'><center><br>
S
}

sub main1{
    #Intializing variables and gathering information from the form
    my $continue = '';
    my $sumName = param ('sumName');
    
    print "<table border='1' style='width:20%'><tr>";
    if ($sumName) {
        print "<td>";
        print "<center>";
        print "$sumName<br>";
        print "-" x 25;
        print "<br>";
        my $summoner = Summoner::by_name($sumName);
        my $sumId = $summoner->{"id"};
        my $league = League::league($sumId);
        my $matchhistory = Matchhistory::matchhistory($sumId);
        my $stats = Stats::stats($sumId);
        print "$league->{'tier'} $league->{'division'} $league->{'lp'}LP: $league->{'name'}<br>";
        printf ("GAMES PLAYED: %d<br>WINS: %d LOSSES: %d<br>TOTAL KDA: %d/%d/%d<br>", $stats->{0}->{"totalSessionsPlayed"}, $stats->{0}->{"totalSessionsWon"}, $stats->{0}->{"totalSessionsLost"}, $stats->{0}->{"totalChampionKills"}, $stats->{0}->{"totalDeathsPerSession"}, $stats->{0}->{"totalAssists"});
        print "-" x 25;
        print "<br>";
        
        print "Recent Games:<br>";
        printf ("Top     - %dG %dW %dL<br>",$matchhistory->{'totalTop'},     $matchhistory->{'topWins'},     $matchhistory->{'totalTop'} -     $matchhistory->{'topWins'});
        printf ("Jungle  - %dG %dW %dL<br>",$matchhistory->{'totalJG'},      $matchhistory->{'jgWins'},      $matchhistory->{'totalJG'} -      $matchhistory->{'jgWins'});
        printf ("Middle  - %dG %dW %dL<br>",$matchhistory->{'totalMid'},     $matchhistory->{'midWins'},     $matchhistory->{'totalMid'} -     $matchhistory->{'midWins'});
        printf ("ADC     - %dG %dW %dL<br>",$matchhistory->{'totalADC'},     $matchhistory->{'adcWins'},     $matchhistory->{'totalADC'} -     $matchhistory->{'adcWins'});
        printf ("Support - %dG %dW %dL<br>",$matchhistory->{'totalSupport'}, $matchhistory->{'supportWins'}, $matchhistory->{'totalSupport'} - $matchhistory->{'supportWins'});
        print "-" x 25;
        print "<br>";
        
        for (my $i = 1; $i < ($matchhistory->{'totalGamesPlayed'}) + 1; $i++){
            my $id         = $matchhistory->{'championData'}->{$i}->{'id'};
            my $kills      = $matchhistory->{'championData'}->{$i}->{'kills'};
            my $deaths     = $matchhistory->{'championData'}->{$i}->{'deaths'};
            my $assists    = $matchhistory->{'championData'}->{$i}->{'assists'};
            my $creepScore = $matchhistory->{'championData'}->{$i}->{'creepScore'};
            my $outcome    = $matchhistory->{'championData'}->{$i}->{'outcome'};
            my $champion = Champion::champion($id);
            my $role = $matchhistory->{'championData'}->{$i}->{'role'};
            
            if ($outcome eq "true"){
                    $outcome = "WIN";
            }elsif ($outcome eq "false"){
                    $outcome = "LOST";
            }
            printf ("%d. %s \@ %s<br>CHAMPION: %s<br>KDA: %d/%d/%d<br>CS: %d<br>", $i, $outcome, $role, $champion, $kills, $deaths, $assists, $creepScore);
            print "-" x 10;
            print "<br>";
        }
        print "</center>";
        print "</td>";
    }
    
    return <<S;
    <form action ='$continue' method='get'>
        <center>Enter a summoner name: <input type='text' name='sumName' value='$sumName'></center><br>
        <center>
            <input type='submit' value='search'>
            <a href='http://matrix.senecac.on.ca/~apmacdonald/lolatmyteam_single.cgi'><button type='button'>Reset</button></a>
        </center>
    </form>
    <br></tr></table>
S
}

sub end {
    return <<E;
    </body>
</html>
E
}