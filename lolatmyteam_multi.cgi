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
print main();
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
sub end {
    return <<E;
    </body>
</html>
E
}

sub main {
    my $sumName1 = param('sumName1');
    my $sumName2 = param('sumName2');
    my $sumName3 = param('sumName3');
    my $sumName4 = param('sumName4');
    my $sumName5 = param('sumName5');
    
    print "<form action='' method='get'>";
    print "<table border='1' style='width:100%'>";
    
        #The header row for input
        print"<tr>";
            print"<th>";
                print "<center>Summoner 1: <input type='text' name='sumName1' value =$sumName1></center>";
            print"</th>";
            
            print"<th>";
                print "<center>Summoner 2: <input type='text' name='sumName2' value =$sumName2></center>";
            print"</th>";
            
            print"<th>";
                print "<center>Summoner 3: <input type='text' name='sumName3' value =$sumName3></center>";
            print"</th>";
            
            print"<th>";
                print "<center>Summoner 4: <input type='text' name='sumName4' value =$sumName4></center>";
            print"</th>";
            
            print"<th>";
                print "<center>Summoner 5: <input type='text' name='sumName5' value =$sumName5></center>";
            print"</th>";
        print"</tr>";
        
        print "<tr>";
            print "<td>";
                print printData($sumName1);
            print "</td>";
            
            print "<td>";
                print printData($sumName2);
            print "</td>";
            
            print "<td>";
                if ($sumName2) {
                    sleep(7);
                    print printData($sumName3);
                }
            print "</td>";
            
            print "<td>";
                if ($sumName3) {
                    sleep(7);
                    print printData($sumName4);
                }
            print "</td>";
            
            print "<td>";
                if ($sumName4) {
                    sleep(7);
                    print printData($sumName5);
                }
            print "</td>";
        print "</tr>";
    print "</table>";
    print "<button type='submit' name='search'>search</button>";
    print "</form>";
    print "<a href='http://matrix.senecac.on.ca/~apmacdonald/lolatmyteam_multi.cgi'><button type='button'>reset</button></a>";
    
    return;
}

sub printData{
    my ($sumName) = @_;
    if ($sumName) {
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
        print "<center>";
    }
    return;
}

