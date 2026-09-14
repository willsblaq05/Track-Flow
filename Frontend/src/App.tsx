import { useState } from 'react'
import type { FormEvent } from 'react'

function App() {
  const [trackingNumber, setTrackingNumber] = useState('TF-2048-881')
  const [searchedNumber, setSearchedNumber] = useState('TF-2048-881')

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setSearchedNumber(trackingNumber.trim() || 'TF-2048-881')
  }

  return (
    <main className="min-h-screen bg-[#f2f5f0] text-[#17211f]">
      <nav className="mx-auto flex max-w-6xl items-center justify-between px-6 py-7 lg:px-10">
        <div className="flex items-center gap-3 font-bold tracking-tight">
          <span className="grid h-9 w-9 place-items-center rounded-full bg-[#d8f04a] text-lg">+</span>
          <span className="text-xl">TrackFlow</span>
        </div>
        <span className="font-mono text-xs uppercase tracking-[0.2em] text-[#68726e]">Logistics / 01</span>
      </nav>

      <section className="mx-auto grid max-w-6xl gap-12 px-6 pb-16 pt-16 lg:grid-cols-[1.05fr_0.95fr] lg:items-end lg:px-10 lg:pt-24">
        <div>
          <p className="mb-6 font-mono text-xs uppercase tracking-[0.25em] text-[#77837c]">Public shipment tracking</p>
          <h1 className="max-w-3xl text-5xl font-extrabold leading-[0.98] tracking-[-0.06em] sm:text-7xl">Know where it is. Know what is next.</h1>
          <p className="mt-7 max-w-lg text-lg leading-8 text-[#68726e]">One clear view of every handoff, hub, and mile between your shipment and its destination.</p>
        </div>
        <form onSubmit={handleSubmit} className="border-t-2 border-[#17211f] pt-5">
          <label className="font-mono text-xs uppercase tracking-[0.2em] text-[#77837c]" htmlFor="tracking-number">Enter tracking number</label>
          <div className="mt-4 flex gap-3">
            <input id="tracking-number" value={trackingNumber} onChange={(event) => setTrackingNumber(event.target.value)} className="min-w-0 flex-1 border-b border-[#aeb8b0] bg-transparent px-0 py-3 font-mono text-lg outline-none placeholder:text-[#aeb8b0] focus:border-[#17211f]" />
            <button className="rounded-full bg-[#17211f] px-6 py-3 font-semibold text-[#f2f5f0] transition hover:bg-[#39504a]" type="submit">Track <span aria-hidden="true">↗</span></button>
          </div>
        </form>
      </section>

      <section className="mx-auto max-w-6xl px-6 pb-16 lg:px-10">
        <div className="grid overflow-hidden rounded-2xl bg-[#17211f] text-[#f2f5f0] lg:grid-cols-[1.1fr_0.9fr]">
          <div className="p-8 sm:p-12">
            <div className="flex items-center justify-between border-b border-[#53625d] pb-7"><span className="font-mono text-xs uppercase tracking-[0.2em] text-[#aeb8b0]">Shipment {searchedNumber}</span><span className="rounded-full bg-[#d8f04a] px-3 py-1 text-xs font-bold text-[#17211f]">In transit</span></div>
            <div className="mt-14"><p className="font-mono text-xs uppercase tracking-[0.2em] text-[#aeb8b0]">Current location</p><h2 className="mt-3 text-4xl font-bold tracking-[-0.04em]">Cincinnati, OH</h2><p className="mt-3 text-[#aeb8b0]">Moving toward the Columbus regional hub</p></div>
            <div className="mt-16 grid grid-cols-2 gap-8 border-t border-[#53625d] pt-6"><div><p className="font-mono text-xs uppercase text-[#aeb8b0]">Est. delivery</p><p className="mt-2 text-xl font-semibold">Oct 18, 2026</p></div><div><p className="font-mono text-xs uppercase text-[#aeb8b0]">Last update</p><p className="mt-2 text-xl font-semibold">14 min ago</p></div></div>
          </div>
          <div className="relative min-h-72 overflow-hidden bg-[#d8f04a] p-8 text-[#17211f] sm:p-12"><div className="absolute -right-20 -top-24 h-72 w-72 rounded-full border-[3px] border-[#17211f]/15" /><div className="absolute -bottom-32 -left-12 h-80 w-80 rounded-full border-[3px] border-[#17211f]/15" /><p className="relative font-mono text-xs uppercase tracking-[0.2em]">Route progress</p><div className="relative mt-20 flex items-center gap-3"><span className="h-4 w-4 rounded-full bg-[#17211f]" /><span className="h-0.5 flex-1 bg-[#17211f]" /><span className="h-4 w-4 rounded-full border-2 border-[#17211f] bg-[#d8f04a]" /></div><div className="relative mt-4 flex justify-between text-sm font-semibold"><span>Memphis, TN</span><span>Columbus, OH</span></div></div>
        </div>
      </section>
    </main>
  )
}

export default App
