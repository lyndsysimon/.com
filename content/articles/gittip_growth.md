Title: Gittip Growth
Category: Programming

If you've not heard of it, Gittip is a site designed to help open source
developers build an income independent of traditional employers, based instead
on small anonymous donations from others who benefit from their work and want
to show their appreciation and enable them to continue to produce for the
community.

Gittip bills itself as a "personal funding platform." I personally believe that
this site will change the world. The site was created by Chad Whitacre , who I
met this year at PyOhio. His enthusiasm for the project (and the philosophy surrounding it) is downright infectious.

I've been watching to see how Gittip gains adoption, and decided to put up a
very quick graph of the trend. It's coming along nicely!

<script>
    $(function() {
        function init_charts() {
            $('#paydays_chart').kendoChart({
                dataSource: {
                    data: paydays
                }
                , chartArea: {
                    height: 220
                }
                , series:[
                    {
                        field:'transfer_volume'
                        , name: 'USD Transfered'
                        , type: 'line'
                        , tooltip: {
                            visible: true
                            , format: 'C'
                        }
                    }
                ]
                , legend: {
                    position:'bottom'
                }
                , categoryAxis: {
                    field: 'ts_start'
                    , labels: {
                        template: '#= value.substring(0,10) #'
                        , rotation:90
                    }
                }
                , valueAxis: {
                    labels: {
                        format: 'C'
                    }
                }
            })
        }
        $.getJSON('https://www.gittip.com/about/paydays.json', function(data) {
                paydays = data.reverse();
                if (paydays.length > 18) {
                    paydays.length = 18
                }
                init_charts();
            })
        })

</script>

<div id='paydays_chart'></div>