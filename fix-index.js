const fs = require('fs');

let c = fs.readFileSync('public/index.html', 'utf8');

const search = `      background-attachment: fixed;
      <div class="metallic-shine-layer"></div>`;

const replace = `      background-attachment: fixed;
    }
  </style>
</head>

<body>
  <script>
    if (sessionStorage.getItem('hasSeenLogoReveal')) {
      document.write('<style>#introScreen { display: none !important; } #mainWebsite { display: block !important; opacity: 1 !important; }</style>');
    }
  </script>
  <!-- METALLIC CODE REVEAL INTRO -->
  <div class="intro-container" id="introScreen">
    <div class="metallic-logo-wrapper">
      <img width="800" height="685" src="images/products/kvb-logo.webp" alt="KVB Logo" class="metallic-logo-img" fetchpriority="high">
      <div class="metallic-shine-layer"></div>`;

// Try exact match first
if (c.includes(search)) {
    c = c.replace(search, replace);
} else {
    // Try with different line endings
    const searchCRLF = search.replace(/\n/g, '\r\n');
    if (c.includes(searchCRLF)) {
        c = c.replace(searchCRLF, replace.replace(/\n/g, '\r\n'));
    } else {
        const searchLF = search.replace(/\r\n/g, '\n');
        if (c.includes(searchLF)) {
            c = c.replace(searchLF, replace.replace(/\r\n/g, '\n'));
        }
    }
}

fs.writeFileSync('public/index.html', c, 'utf8');
console.log('Fixed index.html!');
