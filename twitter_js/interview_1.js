define('dataKonami', function () {
    return flight.component(function Konami() {
        this.after('initialize', function () {
            var code = [38,38,40,40,37,39,37,39,66,65];
            var count = 0;

            this.on('keydown', function konamiKeydown(e) {
                var kstr;
                var keyCode = e.keyCode;
                
                if (code[count] === e.keyCode) {
                    count++;
                    if (count === code.length) {
                        this.trigger('uiKonami');
                        count = 0;
                    }
                } else {
                    count = 0;
                }
            }.bind(this));
        });
    });
});

define('konamiBtn', function () {
    return flight.component(function KonamiBtn() {
        this.defaultAttrs({
            btnSelector: '.js-fake-konami'
        });
        
        this.after('initialize', function () {
            this.on('click', {
                btnSelector: function () {
                    this.trigger('uiKonami');
                }
            });
        });
    });
});

define('wowEasteregg', function () {
    return flight.component(function WowEasteregg() {
        this.defaultAttrs({
            // How many wows per invocation?
            numberOfWows: 10,

            // Total duration in milliseconds
            duration: 5000,

            // CSS Class -> Inner Content
            wows: {
                'wow-blue wow-text': 'such konami',
                'wow-green wow-text': 'wow',
                'wow-red wow-text': 'amaze',
                'wow-dogenut': '',
                'wow-lion': '',
                'wow-rainwow': ''
            }
        });

        this.after('initialize', function () {
            this.on(document, 'uiKonami', this.handleKonami);
        });


        // Pick random wowsa
        var keys = Object.keys(this.attr.wows);
        var waitMs = 1000 * this.attr.numberOfWows;
        
        this.makeWow = function () {
            // Idea: Math.round() for fun undefined errors
            var cls = keys[Math.floor(Math.random() * keys.length)];
            var text = this.attr.wows[cls];
            var $div = $('<div>').text(text);
            // Add the 'wow' class in addition to the ones described above.
            if (cls !== '') {
                $div.addClass('wow').addClass(cls);
            }

            // Put it into the DOM at some point
            setTimeout(this.insertWow.bind(this, $div),
                       waitMs * Math.random());
        };

        this.handleKonami = function () {
            var numWows = this.attr.numberOfWows;
            
            for (var i = 0; i < numWows; i++) {
                this.makeWow();
            }
        };
        
        this.insertWow = function ($element) {
            $element.css({
                left: '20px',
                top: (100 * Math.random() - 25) + '%'
            });

            $element.hide();
            $element.appendTo(document.body);
            $element.fadeIn();

            this.animateWow($element, this.attr.duration, null);
        };

        this.animateWow = function ($element, duration, start) {
            var timestamp = ~~new Date();
            start = start || timestamp;

            var width = $(document).outerWidth();
            var progress = (timestamp - start) / duration;

            $element.css({
                left: Math.min(width, width * progress),
                webkitTransform: 'rotate(' + progress * 3 + 'turn)',
                transform: 'rotate(' + progress * 3 + 'turn)'
            });

            setTimeout(function () {
                this.animateWow($element, duration, start);
            }.bind(this), 1 / 16);
        };
    });
});

define('defaultPage', ['dataKonami', 'konamiBtn', 'wowEasteregg'], function (dataKonami, konamiBtn, wowEasterEgg) {
    return flight.component(function defaultPage() {
        this.after('initialize', function () {
            dataKonami.attachTo(document);
            
            konamiBtn.attachTo(this.$node);
            wowEasterEgg.attachTo(this.$node);
        });
    });
});

require(['./defaultPage'], function (defaultPage) {
    defaultPage.attachTo(document.querySelector('#main'));
});
